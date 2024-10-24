import { useState } from "react";
import ChatBubble from "./ChatBubble.jsx";
import "../styles/components/ChatHistory.css";

const historyStart = [
  {
    sender: "bot",
    img: "",
    message: "Bienvenido al chat, ¿Cómo te puedo ayudar?",
  },
];

export default function ChatHistory() {
  const [history, setHistory] = useState(historyStart);

  return (
    <div className="chat-history">
      {history.map((h, i) => (
        <ChatBubble key={`${i}-${h.sender}`} {...h} />
      ))}
    </div>
  );
}
