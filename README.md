# ChatSim

Static GenAI chat simulator for presentations.

## Usage

1. Run `npm start` in `C:\develop\ChatSim`.
2. Open `http://localhost:3000/chatsim.html`.
3. Press `Start Demo`.
4. Use `Space` or `Right Arrow` to advance.
5. Use `R` to restart.

## What it includes

- Staged user and assistant messages
- Typing animation for assistant replies
- Full-screen popup moments for presenter emphasis
- Sidebar step navigation
- Progress indicator and restart flow

## Customization

Edit [chatData.json](/C:/develop/ChatSim/chatData.json) to change:

- Demo title
- Model label
- Step content
- Timing values

The page loads `chatData.json` over HTTP, so opening `chatsim.html` directly as a `file://` page will not work.
