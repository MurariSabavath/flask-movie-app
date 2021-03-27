const dayBtn = document.querySelector(".day-btn");
const weekBtn = document.querySelector(".week-btn");

document.querySelector(".icon").addEventListener("click", () => {
  const x = document.getElementById("myTopnav");
  if (x.className === "topnav") {
      x.className += " responsive";
    } else {
      x.className = "topnav";
    }
})

dayBtn.addEventListener("click", () => {
    document.querySelector(".trending-day").style.display = 'block';
    document.querySelector(".trending-week").style.display = 'none';
    weekBtn.classList.remove('active');
    dayBtn.classList.add("active");
})

weekBtn.addEventListener("click", () => {
    document.querySelector(".trending-day").style.display = 'none';
    document.querySelector(".trending-week").style.display = 'block';
    weekBtn.classList.add('active');
    dayBtn.classList.remove("active");
})


