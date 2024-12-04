// Desc:
// Author:
// Dates:

var $ = function (id) {
  return document.getElementById(id);
};

// Define format options for printing.
const cur2Format = new Intl.NumberFormat("en-CA", {
  style: "currency",
  currency: "CAD",
  minimumFractionDigits: "2",
  maximumFractionDigits: "2",
});

const per2Format = new Intl.NumberFormat("en-CA", {
  style: "percent",
  minimumFractionDigits: "2",
  maximumFractionDigits: "2",
});

const com2Format = new Intl.NumberFormat("en-CA", {
  style: "decimal",
  minimumFractionDigits: "2",
  maximumFractionDigits: "2",
});

// Start function definitions here.

// Slideshow function and code! :D
let step = 0;
let Images = new Array();
Images[0] = "Images/TeslaBot.jpg";
Images[1] = "Images/BDDog.jpg";
Images[2] = "Images/OilBot.jpg";
Images[3] = "Images/AnotherRobot.jpg";
Images[4] = "Images/MilitaryBot.jpg";
window.onload = setInterval(gallery, 4000);


function gallery() {
    document.getElementById("imgSlide").src = Images[step];

    if(step < Images.length - 1) {
        step++;
    } else {
        step = 0;
    }
}
//