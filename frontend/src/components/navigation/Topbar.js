import MenuIcon from "../icons/MenuIcon";
import FoodIcon from "../icons/FoodIcon";
import { NavLink } from "react-router";

const Topbar = ({ onOpenMenu }) => {
  return (
    <div className="fixed flex items-center justify-between gap-4 p-6 pt-10 lg:hidden h-5 w-full">
      <button onClick={onOpenMenu}>
        <MenuIcon />
      </button>
      <NavLink
        to="/"
        className="flex gap-2 font-bold text-red-950 fill-red-950"
      >
        <FoodIcon />
        <h1 className="font-bold">Kokboken</h1>
      </NavLink>
    </div>
  );
};

export default Topbar;
