import { useState } from "react";
import { useIsDesktop } from "../../hooks/useIsDesktop";
import Drawer from "@mui/material/Drawer";
import Sidebar from "./Sidebar";
import Topbar from "./Topbar";

const Navbar = () => {
  const isDesktop = useIsDesktop();
  const [sidebarOpen, setSidebarOpen] = useState(false);

  const toggleSidebar = () => {
    setSidebarOpen(!sidebarOpen);
  };

  return (
    <>
      {isDesktop ? (
        <Sidebar />
      ) : (
        <>
          <Topbar onOpenMenu={toggleSidebar} />
          <Drawer
            variant="temporary"
            open={sidebarOpen}
            onClose={toggleSidebar}
            ModalProps={{ keepMounted: true }}
          >
            <Sidebar onClose={toggleSidebar} />
          </Drawer>
        </>
      )}
    </>
  );
};

export default Navbar;
