import "../styles/components/Button.css";

export default function Button(props) {
  const { onClick, label } = props;

  return (
    <button className="btn" onClick={onClick}>
      {label}
    </button>
  );
}
