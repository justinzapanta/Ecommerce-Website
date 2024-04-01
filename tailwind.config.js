/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./seller/templates/seller/*.html'],
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

