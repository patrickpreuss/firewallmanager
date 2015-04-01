var doughnutProtoData = [
	{
		value: {{ badcount }},
		color:"#E9573F",
		highlight: "#FC6E51",
		label: "Failed Rules"
	},
	{
		value: {{ goodcount }},
		color: "#8CC152",
		highlight: "#A0D468",
		label: "Succesfull Rules"
	},

];
var doughnutData = [
	{
		value: {{ tcpcount }},
		color:"#D770AD",
		highlight: "#EC87C0",
		label: "TCP Rules"
	},
	{
		value: {{ udpcount }},
		color: "#967ADC",
		highlight: "#AC92EC",
		label: "UDP Rules"
	},
	{
		value: {{ icmpcount }},
		color: "#37BC9B",
		highlight: "#48CFAD",
		label: "ICMP Rules"
	},

];

window.onload = function(){
	var ctxproto = document.getElementById("chartProto").getContext("2d");
	window.myDoughnut = new Chart(ctxproto).Pie(doughnutData, {responsive : true});

	var ctx = document.getElementById("chartStatus").getContext("2d");
	window.myDoughnut = new Chart(ctx).Pie(doughnutProtoData, {responsive : true});
}
