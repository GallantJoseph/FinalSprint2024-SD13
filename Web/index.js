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
