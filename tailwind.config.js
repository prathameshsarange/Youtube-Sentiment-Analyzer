/** @type {import('tailwindcss').Config} */
module.exports = {
  darkMode: "class",
  content: ["./templates/**/*.html"],
  theme: {
    extend: {
      colors: {
        "surface-container-lowest": "#060e20",
        "secondary": "#89ceff",
        "on-surface-variant": "#c7c4d7",
        "tertiary-fixed": "#e9ddff",
        "on-secondary-container": "#00344e",
        "surface-container-low": "#131b2e",
        "surface": "#0b1326",
        "on-secondary": "#00344d",
        "primary-fixed": "#e1e0ff",
        "background": "#0b1326",
        "tertiary-fixed-dim": "#d0bcff",
        "on-background": "#dae2fd",
        "primary": "#c0c1ff",
        "secondary-fixed": "#c9e6ff",
        "surface-container-highest": "#2d3449",
        "tertiary": "#d0bcff",
        "secondary-container": "#00a2e6",
        "inverse-on-surface": "#283044",
        "secondary-fixed-dim": "#89ceff",
        "on-error-container": "#ffdad6",
        "surface-variant": "#2d3449",
        "on-secondary-fixed": "#001e2f",
        "on-tertiary-fixed-variant": "#5516be",
        "on-tertiary-fixed": "#23005c",
        "inverse-primary": "#494bd6",
        "on-primary": "#1000a9",
        "surface-container-high": "#222a3d",
        "on-primary-fixed": "#07006c",
        "surface-bright": "#31394d",
        "surface-dim": "#0b1326",
        "on-secondary-fixed-variant": "#004c6e",
        "surface-tint": "#c0c1ff",
        "primary-container": "#8083ff",
        "surface-container": "#171f33",
        "outline-variant": "#464554",
        "on-tertiary-container": "#340080",
        "inverse-surface": "#dae2fd",
        "error-container": "#93000a",
        "on-tertiary": "#3c0091",
        "on-error": "#690005",
        "primary-fixed-dim": "#c0c1ff",
        "outline": "#908fa0",
        "on-surface": "#dae2fd",
        "on-primary-fixed-variant": "#2f2ebe",
        "on-primary-container": "#0d0096",
        "error": "#ffb4ab",
        "tertiary-container": "#a078ff"
      },
      spacing: {
        "base": "8px",
        "container-max-width": "1440px",
        "section-gap": "128px",
        "gutter": "24px",
        "margin-desktop": "64px",
        "margin-mobile": "16px"
      },
      fontFamily: {
        "label-md": ["JetBrains Mono"],
        "label-sm": ["JetBrains Mono"],
        "body-md": ["Geist"],
        "display-lg-mobile": ["Sora"],
        "body-lg": ["Geist"],
        "display-lg": ["Sora"],
        "headline-md": ["Sora"],
        "headline-lg": ["Sora"]
      },
      fontSize: {
        "label-md": ["14px", { "lineHeight": "1.4", "letterSpacing": "0.05em", "fontWeight": "500" }],
        "label-sm": ["12px", { "lineHeight": "1.4", "letterSpacing": "0.03em", "fontWeight": "500" }],
        "body-md": ["16px", { "lineHeight": "1.6", "fontWeight": "400" }],
        "display-lg-mobile": ["32px", { "lineHeight": "1.2", "fontWeight": "700" }],
        "body-lg": ["18px", { "lineHeight": "1.6", "fontWeight": "400" }],
        "display-lg": ["48px", { "lineHeight": "1.1", "letterSpacing": "-0.02em", "fontWeight": "700" }],
        "headline-md": ["24px", { "lineHeight": "1.3", "fontWeight": "600" }],
        "headline-lg": ["32px", { "lineHeight": "1.2", "fontWeight": "600" }]
      }
    }
  },
  plugins: [
    require("@tailwindcss/forms"),
    require("@tailwindcss/container-queries")
  ]
};
