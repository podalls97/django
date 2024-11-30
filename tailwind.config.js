/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './templates/**/*.html', // Adjust if you use different template paths
    './dashboard/templates/**/*.html', // Include app-specific templates
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}
