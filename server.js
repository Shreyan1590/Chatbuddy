const express = require("express");
const cors = require("cors");

const app = express();
app.use(cors());
app.use(express.json());

let userName = "";

const chatbotResponses = {
    "hello": "Hi there! How can I assist you?",
    "how are you": "I'm just a bot, but I'm doing great! How about you?",
    "what's your name": "I'm ChatBuddy, your friendly AI assistant!",
    "bye": "Goodbye! Have a wonderful day!",
    "tell me a joke": "Why don’t skeletons fight each other? Because they don’t have the guts! Haha!"
};

function correctSpelling(input) {
    const corrections = {
        "helllo": "hello",
        "hwo": "how",
        "whta": "what",
        "naem": "name",
        "godo": "good",
        "byee": "bye"
    };
    return corrections[input] || input;
}

app.post("/chat", (req, res) => {
    let userMessage = req.body.message.trim();
    if (!userMessage) return res.json({ response: "Please enter a message." });

    let lowerMessage = userMessage.toLowerCase();
    lowerMessage = correctSpelling(lowerMessage);
    let botReply;

    if (lowerMessage.startsWith("my name is")) {
        userName = userMessage.split(" ").slice(3).join(" ");
        botReply = `Nice to meet you, ${userName}! How can I assist you today?`;
    } else if (lowerMessage.includes("my name")) {
        botReply = "Could you please tell me your name in the format 'My name is [Your Name]'?";
    } else if (userName && chatbotResponses[lowerMessage]) {
        botReply = chatbotResponses[lowerMessage].replace("Hi there!", `Hi ${userName}!`);
    } else {
        botReply = chatbotResponses[lowerMessage] || "I'm not sure how to respond to that.";
    }

    res.json({ response: botReply });
});

// Set Vercel Port
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
