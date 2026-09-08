const chatBox = document.getElementById("chatBox");
const userInput = document.getElementById("userInput");
const sendButton = document.getElementById("sendButton");


function addMessage(message, sender) {
    const messageDiv = document.createElement("div");
    messageDiv.classList.add("message", `${sender}-message`);

    const contentDiv = document.createElement("div");
    contentDiv.classList.add("message-content");

    const name = document.createElement("strong");
    name.textContent = sender === "user" ? "You" : "Bot";

    const text = document.createElement("p");
    text.textContent = message;

    contentDiv.appendChild(name);
    contentDiv.appendChild(text);

    messageDiv.appendChild(contentDiv);
    chatBox.appendChild(messageDiv);

    chatBox.scrollTop = chatBox.scrollHeight;
}


async function sendMessage() {
    const message = userInput.value.trim();
    if (!message) {
        return;
    }


    addMessage(message, "user");

    userInput.value = "";

    const exitMessages = [
        "quit",
        "exit",
        "bye",
        "goodbye"
    ];

    if (exitMessages.includes(message.toLowerCase())) {
        addMessage(
            "Thanks for using TechAssist! 👋 Have a great day!",
            "bot"
        );

        return;
    }

    sendButton.disabled = true;
    sendButton.textContent = "Sending...";

    try {
        const response = await fetch("/chat", {
            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                message: message
            })
        });

        if (!response.ok) {
            throw new Error("Server error");
        }

        const data = await response.json();
        addMessage(data.response, "bot");

    } catch (error) {

        console.error("Error:", error);

        addMessage(
            "Sorry, something went wrong. Please try again.",
            "bot"
        );

    } finally {

        sendButton.disabled = false;
        sendButton.textContent = "Send";

        
        userInput.focus();
    }
}


sendButton.addEventListener("click", sendMessage);



userInput.addEventListener("keydown", function(event) {

    if (event.key === "Enter") {
        sendMessage();
    }

});


userInput.focus();