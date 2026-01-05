import { NavLink } from "react-router";
import Placeholder from "../assets/sebbe.png";

const ProfileAvatar = ({ onClick }) => {
  return (
    <NavLink
      to="/mina-sidor"
      className="flex flex-col items-center"
      onClick={onClick}
    >
      {({ isActive }) => (
        <img
          className={`rounded-full w-16 h-16 ${
            isActive && "outline outline-2 outline-offset-4 outline-pink-800 "
          }`}
          src={Placeholder}
        ></img>
      )}
    </NavLink>
  );
};

export default ProfileAvatar;
