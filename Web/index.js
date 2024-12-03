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

function LoanAnalysis() {
	// Template
	document.getElementById("loan").innerHTML = `
    <p>Loan Analysis Statement</p>
		<br />
		<p>10 year options on $#,###.##</p>
		<p>Reason: Xxxxxxxx Xxxxxxxxx Xxxxxxxxxx</p>
		<p>Statement date: YYYY-MM-DD</p>
		<br />
		<p>Years&nbsp;&nbsp;Interest&nbsp;&nbsp;Total Amt&nbsp;&nbsp;Mon Payment</p>
		<p>---------------------------------------</p>
		<p>&nbsp;##&nbsp;&nbsp;&nbsp;$#,###.##&nbsp;&nbsp;$#,###.##&nbsp;&nbsp;&nbsp;$#,###.##</p>
		<p>&nbsp;##&nbsp;&nbsp;&nbsp;$#,###.##&nbsp;&nbsp;$#,###.##&nbsp;&nbsp;&nbsp;$#,###.##</p>
		<p>&nbsp;##&nbsp;&nbsp;&nbsp;$#,###.##&nbsp;&nbsp;$#,###.##&nbsp;&nbsp;&nbsp;$#,###.##</p>
		<p>&nbsp;##&nbsp;&nbsp;&nbsp;$#,###.##&nbsp;&nbsp;$#,###.##&nbsp;&nbsp;&nbsp;$#,###.##</p>
		<p>&nbsp;##&nbsp;&nbsp;&nbsp;$#,###.##&nbsp;&nbsp;$#,###.##&nbsp;&nbsp;&nbsp;$#,###.##</p>
		<p>&nbsp;##&nbsp;&nbsp;&nbsp;$#,###.##&nbsp;&nbsp;$#,###.##&nbsp;&nbsp;&nbsp;$#,###.##</p>
		<p>&nbsp;##&nbsp;&nbsp;&nbsp;$#,###.##&nbsp;&nbsp;$#,###.##&nbsp;&nbsp;&nbsp;$#,###.##</p>
		<p>&nbsp;##&nbsp;&nbsp;&nbsp;$#,###.##&nbsp;&nbsp;$#,###.##&nbsp;&nbsp;&nbsp;$#,###.##</p>
		<p>&nbsp;##&nbsp;&nbsp;&nbsp;$#,###.##&nbsp;&nbsp;$#,###.##&nbsp;&nbsp;&nbsp;$#,###.##</p>
		<p>&nbsp;##&nbsp;&nbsp;&nbsp;$#,###.##&nbsp;&nbsp;$#,###.##&nbsp;&nbsp;&nbsp;$#,###.##</p>
		<p>---------------------------------------</p>
		<p>Payback option selected:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;## Years</p>
    <button onclick="LoanPrep()">Clear</button>
  `;
	return;
}

function LoanPrep() {
	document.getElementById("loan").innerHTML = `
  <button onclick="LoanAnalysis()">Loan Analysis</button>
  `;
	return;
}
