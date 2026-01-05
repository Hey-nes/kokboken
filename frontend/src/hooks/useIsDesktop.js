import { useEffect, useState } from "react";

export const useIsDesktop = () => {
  const query = "(min-width: 1024px)";

  const [isLarge, setIsLarge] = useState(
    typeof window !== "undefined" ? window.matchMedia(query).matches : false
  );

  useEffect(() => {
    const media = window.matchMedia(query);
    const listener = () => setIsLarge(media.matches);

    media.addEventListener("change", listener);
    return () => media.removeEventListener("change", listener);
  }, []);

  return isLarge;
};
