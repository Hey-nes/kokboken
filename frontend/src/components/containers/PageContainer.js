const PageContainer = ({ children }) => {
  return (
    <div className="flex flex-col w-full items-center gap-8 font-bold text-4xl p-6 pt-20 md:p-10 md:pt-20">
      {children}
    </div>
  );
};

export default PageContainer;
