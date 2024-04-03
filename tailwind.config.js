/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./main/templates/main/shop/*.html'],
  theme: {
    extend: {
      'colors' : {
        'model-background' : {
        'gray' : '#686868'
        }
      }
    },
  },
  plugins: [],
}

