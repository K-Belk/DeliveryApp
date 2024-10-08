/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./app/**/*.{js,jsx,ts,tsx}", "./components/**/*.{js,jsx,ts,tsx}"],
  theme: {
    extend: {
      colors: {
        primary: "#161622",
        secondary: {
          DEFAULT: "#FF9C01",
          100: "#FF9001",
          200: "#FF8E01",
        },
        black: {
          DEFAULT: "#000",
          100: "#1E1E2D",
          200: "#232533",
        },
        gray: {
          DEFAULT: "#8E8E9B",
          100: "#CDCDE0",
          200: "#F5F5F8",
        },
        white: {
          DEFAULT: "#FFF",
          100: "#F7F7F7",
          200: "#F9F9F9",
        },
      },
      fontFamily: {
        primary: ["Aktiv Grotesk"],
      },
    },
  },
  plugins: [],
};