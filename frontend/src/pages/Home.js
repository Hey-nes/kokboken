import TextField from "@mui/material/TextField";
import PageContainer from "../components/containers/PageContainer";

const Home = () => {
  return (
    <PageContainer>
      <h1>Sök recept</h1>
      <TextField
        className="w-full md:w-[500px] lg:w-[700px]"
        placeholder="Sök efter recept..."
        variant="outlined"
        slotProps={{
          input: {
            sx: {
              paddingLeft: "20px",
              borderRadius: "40px",
              background: "white",
            },
          },
        }}
      />
    </PageContainer>
  );
};

export default Home;
