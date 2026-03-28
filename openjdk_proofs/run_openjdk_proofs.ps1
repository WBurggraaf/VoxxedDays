param(
    [Parameter(Mandatory = $true)]
    [string]$BeforeJavaHome,

    [Parameter(Mandatory = $true)]
    [string]$AfterJavaHome,

    [ValidateSet('all', 'threadmxbean-current-user-time', 'formatter-simple-fastpath', 'formatter-localized-numbers', 'collections-bulk-copy')]
    [string]$Case = 'all',

    [int]$Iterations = 300000,

    [int]$Threads = 16,

    [string]$OutputDir = 'openjdk_proofs/output',

    [switch]$SkipJfr
)

$ErrorActionPreference = 'Stop'

$root = Split-Path -Parent $PSScriptRoot
$srcDir = Join-Path $PSScriptRoot 'src'
$buildDir = Join-Path $PSScriptRoot 'build'
$classesDir = Join-Path $buildDir 'classes'

New-Item -ItemType Directory -Force -Path $classesDir | Out-Null

$javac = (Get-Command javac -ErrorAction Stop).Source
& $javac -d $classesDir (Join-Path $srcDir 'OpenJdkProofCases.java')

$cases = if ($Case -eq 'all') {
    @(
        'threadmxbean-current-user-time',
        'formatter-simple-fastpath',
        'formatter-localized-numbers',
        'collections-bulk-copy'
    )
} else {
    @($Case)
}

function Invoke-ProofRun {
    param(
        [string]$Label,
        [string]$JavaHome,
        [string]$CaseName
    )

    $java = Join-Path $JavaHome 'bin\\java.exe'
    if (-not (Test-Path $java)) {
        throw "java.exe not found under $JavaHome"
    }

    $targetDir = Join-Path (Join-Path $root $OutputDir) (Join-Path $CaseName $Label)
    New-Item -ItemType Directory -Force -Path $targetDir | Out-Null

    $stdoutPath = Join-Path $targetDir 'stdout.txt'
    $summaryPath = Join-Path $targetDir 'summary.json'
    $jfrPath = Join-Path $targetDir 'profile.jfr'

    $args = @()
    if (-not $SkipJfr) {
        $args += "-XX:StartFlightRecording=filename=$jfrPath,settings=profile,dumponexit=true"
    }
    $args += '-cp'
    $args += $classesDir
    $args += 'OpenJdkProofCases'
    $args += $CaseName
    $args += $Iterations.ToString()
    if ($CaseName -eq 'threadmxbean-current-user-time') {
        $args += $Threads.ToString()
    }

    $output = & $java @args
    $output | Set-Content -Path $stdoutPath -Encoding UTF8

    $map = @{}
    foreach ($line in $output) {
        if ($line -match '^([^=]+)=(.+)$') {
            $map[$matches[1]] = $matches[2]
        }
    }

    $summary = [ordered]@{
        label = $Label
        case = $CaseName
        java_home = $JavaHome
        elapsed_ns = [long]$map['ELAPSED_NS']
        ops = [long]$map['OPS']
        ns_per_op = [double]$map['NS_PER_OP']
        threads = [int]$map['THREADS']
        sink = [long]$map['SINK']
        stdout = $stdoutPath
        jfr = if ($SkipJfr) { $null } else { $jfrPath }
    }

    $summary | ConvertTo-Json -Depth 4 | Set-Content -Path $summaryPath -Encoding UTF8
    return $summary
}

foreach ($caseName in $cases) {
    $before = Invoke-ProofRun -Label 'before' -JavaHome $BeforeJavaHome -CaseName $caseName
    $after = Invoke-ProofRun -Label 'after' -JavaHome $AfterJavaHome -CaseName $caseName

    $deltaPct = if ($after.ns_per_op -eq 0) {
        $null
    } else {
        [math]::Round((($before.ns_per_op - $after.ns_per_op) / $after.ns_per_op) * 100.0, 2)
    }

    $combined = [ordered]@{
        case = $caseName
        before = $before
        after = $after
        before_slower_pct_vs_after = $deltaPct
    }

    $caseDir = Join-Path (Join-Path $root $OutputDir) $caseName
    $combined | ConvertTo-Json -Depth 5 | Set-Content -Path (Join-Path $caseDir 'comparison.json') -Encoding UTF8
    Write-Host "$caseName : before $($before.ns_per_op) ns/op, after $($after.ns_per_op) ns/op, before slower vs after = $deltaPct%"
}

