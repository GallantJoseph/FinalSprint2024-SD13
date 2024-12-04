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

function DspHeaderMessage() {
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
    "The only time you fail is when you fall down and stay down.",
    "Keep your face to the sunshine and you cannot see a shadow.",
    "You're braver than you believe, and stronger than you seem, and smarter than you think.",
    "Positive anything is better than negative nothing.",
    "It's not whether you get knocked down, it's whether you get up.",
    "The struggle you're in today is developing the strength you need tomorrow.",
    "Happiness is the only thing that multiplies when you share it.",
    "The happiness of your life depends upon the quality of your thoughts.",
  ];

  let currDate = new Date();

  let year = currDate.getFullYear();
  let month = currDate.getMonth();
  let dayOfWeek = currDate.getDay();
  let day = currDate.getDate();
  let hours = currDate.getHours();

  // Greeting for time of day.

  let timeDayMsg = "Good ";
  if (hours >= 5 && hours <= 10) {
    // 6:00-11:59
    timeDayMsg += "Morning";
  } else if (hours <= 16) {
    // 12:00-17:59
    timeDayMsg += "Afternoon";
  } else if (hours <= 22) {
    // 18:00-23:59
    timeDayMsg += "Evening";
  } else {
    // 00:00-5:59
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

  // Random number to show a quote from a list.
  let randNum = Math.floor(Math.random() * (quotesLst.length - 1));

  document.getElementById("headermessage").innerHTML =
    timeDayMsg + " - " + quotesLst[randNum] + " - " + fullDateStr;
}
