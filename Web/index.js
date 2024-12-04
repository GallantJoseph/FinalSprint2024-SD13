// Desc:
// Author:
// Dates:

var $ = function (id) {
  return document.getElementById(id);
};

// Define format options for printing.
const currencyFormat = new Intl.NumberFormat("en-CA", {
  style: "currency",
  currency: "CAD",
  minimumFractionDigits: "2",
  maximumFractionDigits: "2",
});

const percentageFormat = new Intl.NumberFormat("en-CA", {
  style: "percent",
  minimumFractionDigits: "2",
  maximumFractionDigits: "2",
});

const commaFormat = new Intl.NumberFormat("en-CA", {
  style: "decimal",
  minimumFractionDigits: "2",
  maximumFractionDigits: "2",
});

const dateFormat = new Intl.DateTimeFormat("en-CA", {
  // Formats a given date to YYYY-MM-DD
  dateStyle: "short",
});

function DspHeaderMessage() {
  // Desc: Display the header message.
  // Author: Joseph Gallant
  // Dates: Dec. 3, 2024 - Dec. 4, 2024

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

  // Date string as Day, Month Date, YYYY
  let fullDateStr =
    daysOfWeekLst[dayOfWeek] +
    ", " +
    monthsLst[month] +
    " " +
    day +
    ", " +
    year;

  // Random number to display a quote from a list.
  let randNum = Math.floor(Math.random() * (quotesLst.length - 1));

  document.getElementById("headermessage").innerHTML =
    timeDayMsg + " - " + quotesLst[randNum] + " - " + fullDateStr;
}

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

  if (step < Images.length - 1) {
    step++;
  } else {
    step = 0;
  }
}

function TitleCase(str) {
  str = str.toLowerCase().split(" ");
  for (var i = 0; i < str.length; i++) {
    str[i] = str[i].charAt(0).toUpperCase() + str[i].slice(1);
  }
  return str.join(" ");
}

function LoanAnalysis() {
  // Constants
  const TODAY = new Date();
  const INTEREST_RATE = 0.053;
  const LOANSECTION = document.getElementById("loan");

  // User Input
  let loanAmt = parseFloat(prompt("Enter Loan Amount", "5000"), 10);
  let loanReason = prompt("Enter Reason For Loan", "Robot Army");
  let paybackOption = prompt("Enter Length Of Payment", "10");

  // Display Variables
  let loanAmtDsp = currencyFormat.format(loanAmt);
  let loanReasonDsp = TitleCase(loanReason);
  let todayDsp = dateFormat.format(TODAY);

  let loanDisplay = `
	<p>Loan Analysis Statement</p>
	<br />
	<p>10 Year options on ${loanAmtDsp}</p>
	<p>Reason: ${loanReasonDsp}</p>
	<p>Statement date: ${todayDsp}</p>
	<br />

    <table>
		<tr>
			<th>Years</th>
			<th>Interest</th>
			<th>Total Amt</th>
			<th>Mon Payment</th>
		</tr>

		<tr>
			<td colspan="4">--------------------------------------------</td>
		</tr>
	`;

  for (let years = 1; years <= 10; years++) {
    let interest = loanAmt * INTEREST_RATE * years;
    let total = loanAmt + interest;
    let monthly = total / (years * 12);

    interest = currencyFormat.format(interest);
    total = currencyFormat.format(total);
    monthly = currencyFormat.format(monthly);

    loanDisplay += `
		<tr>
			<td class="centeralign">${years}</td>
			<td class="rightalign">${interest}</td>
			<td class="rightalign">${total}</td>
			<td class="rightalign">${monthly}</td>
		</tr>
		`;
  }

  loanDisplay += `
		<tr>
			<td colspan="4">--------------------------------------------</td>
		</tr>
		<tr>
			<td colspan="3">Payback option selected:</td>
			<td class="rightalign">${paybackOption} Years</td>
		</tr>
	</table>
	<br />
	<button onclick="LoanPrep()">Clear</button>
	`;
  LOANSECTION.innerHTML = loanDisplay;
  return;
}

function LoanPrep() {
  document.getElementById("loan").innerHTML = `
  <button onclick="LoanAnalysis()">Loan Analysis</button>
  `;
  return;
}
