export default function ChatBubble({ sender, img, message }) {
  return (
    <div>
      <img src={img} />
      <p>{sender}</p>
      <p>{message}</p>
    </div>
  );
}
