import { NavLink } from "react-router";
import FoodIcon from "../icons/FoodIcon";
import CloseIcon from "../icons/CloseIcon";
import ProfileAvatar from "../ProfileAvatar";

const Sidebar = ({ onClose }) => {
  const namedRoutes = [
    { route: "/", name: "Startsida" },
    { route: "/skapa-recept", name: "Skapa recept" },
    { route: "/kontakter", name: "Kontakter" },
  ];

  return (
    <div className="flex w-[210px] h-screen bg-red-950 flex-col px-6 py-6 lg:py-12 justify-between text-white ">
      {onClose ? (
        <button onClick={onClose}>
          <CloseIcon />
        </button>
      ) : (
        <NavLink
          to="/"
          className="flex flex-col gap-2 items-center font-bold self-center"
          onClick={onClose}
        >
          <FoodIcon />
          <h1 className="font-bold text-2xl">Kokboken</h1>
        </NavLink>
      )}
      <ul className="flex flex-col text-xl items-center gap-8">
        {namedRoutes.map(({ route, name }, i) => (
          <li key={name}>
            <NavLink
              to={route}
              className={({ isActive }) =>
                isActive
                  ? "underline underline-offset-8 decoration-pink-800"
                  : ""
              }
              onClick={onClose}
            >
              {name}
            </NavLink>
          </li>
        ))}
      </ul>
      <ProfileAvatar onClick={onClose} />
    </div>
  );
};

export default Sidebar;
