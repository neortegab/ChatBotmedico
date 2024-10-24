import ImgButton from "./ImgButton.jsx";
import "../styles/components/ChatInput.css";
import send from "../assets/send.svg";

function sendSymptons() {
  window.alert("TODO");
}

export default function ChatInput() {
  return (
    <div style={{ "border-top": "1px solid black", margin: "2px 0 0 0" }}>
      <p style={{ margin: "10px" }}>Describe tus síntomas</p>
      <div className="chat-input">
        <textarea maxLength={200} />
        <ImgButton src={send} onClick={sendSymptons} />
      </div>
    </div>
  );
}
