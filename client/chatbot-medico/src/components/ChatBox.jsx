import ChatHistory from "./ChatHistory";
import ChatInput from "./ChatInput";
import "../styles/components/ChatBox.css";

export default function ChatBox() {
  return (
    <div className="chat-box">
      <ChatHistory />
      <ChatInput />
    </div>
  );
}
