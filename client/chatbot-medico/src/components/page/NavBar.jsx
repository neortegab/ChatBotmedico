import "../../styles/components/page/Navbar.css";
import ImgButton from "../ImgButton.jsx";
import doctor from "../../assets/doctor.svg";
import hamb from "../../assets/hamburger-menu.svg";

function alert() {
  window.alert("test click");
}

export default function NavBar() {
  return (
    <div className="navbar">
      <ImgButton onClick={alert} src={hamb} />
      <ImgButton onClick={alert} src={doctor} />
    </div>
  );
}
