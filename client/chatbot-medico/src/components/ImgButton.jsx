export default function ImgButton({ src, onClick }) {
  return (
    <div onClick={onClick}>
      <img src={src} height={40} width={40} />
    </div>
  );
}
