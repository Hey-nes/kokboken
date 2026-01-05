import Navbar from "./components/navigation/Navbar";
import { BrowserRouter, Routes, Route } from "react-router";
import CreateRecipe from "./pages/CreateRecipe";
import Contacts from "./pages/Contacts";
import Home from "./pages/Home";
import Profile from "./pages/Profile";

function App() {
  return (
    <BrowserRouter>
      <div className="flex min-h-screen">
        <Navbar />
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/skapa-recept" element={<CreateRecipe />} />
          <Route path="/kontakter" element={<Contacts />} />
          <Route path="/mina-sidor" element={<Profile />} />
        </Routes>
      </div>
    </BrowserRouter>
  );
}

export default App;
