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

function HeaderMessage() {
  // Define the lists for days of the week and months.
  let daysOfWeekLst = [
    "Sunday",
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
  ];

  let monthsLst = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
  ];

  // List of quotes
  let quotesLst = [
    "",
    "The danger of the past was that men became slaves. The danger of the future is that men may become robots.",
    "Robots have solved and will continue to solve so many human problems. Except for all the ones that they cause.",
  ];

  let currDate = new Date();

  let year = currDate.getFullYear();
  let month = currDate.getMonth();
  let dayOfWeek = currDate.getDay();
  let day = currDate.getDate();
  let hours = currDate.getHours();

  let morning = "Morning";
  let afterNoon = "Afternoon";
  let evening = "Evening";
  let night = "Night";

  // Greeting for time of day.

  let timeDayMsg = "Good ";
  if (hours >= 5 && hours <= 10) {
    // 6:00-11:00
    timeDayMsg += "Morning";
  } else if (hours <= 16) {
    // 12:00-17:00
    timeDayMsg += "Afternoon";
  } else if (hours <= 22) {
    // 18:00-23:00
    timeDayMsg += "Evening";
  } else {
    // 00:00-5:00
    timeDayMsg += "Night";
  }

  // Date string as Day, Month date, YYYY
  let fullDateStr =
    daysOfWeekLst[dayOfWeek] +
    ", " +
    monthsLst[month] +
    " " +
    day +
    ", " +
    year;

  let randNum = Math.floor(Math.random() * (quotesLst.length - 1));

  console.log(randNum);

  let quote = (document.getElementById("headermessage").innerHTML =
    timeDayMsg + " - " + quotesLst[1] + " - " + fullDateStr);
}
