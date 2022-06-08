let ChartOne = document.getElementById('ChartOne').getContext("2d");

let barChart = new Chart(ChartOne, {

  type : 'doughnut', // pie, line, doughnut, polarArea
  data : {
    labels : ['positive', 'negative', 'neutral'],
    datasets : [
      {
        label : 'peoples think',
        data:[sentimentData.confidenceScore.positivesentimentData.confidenceScore.positive, sentimentData.confidenceScore.positive.negative, sentimentData.confidenceScore.neutral ],
        backgroundColor: [
  					'#FF5F00',
  					'#B20600',
  					'#00092C',
  				],

    }]
},
options: {
			responsive: false,
			scales: {
				yAxes: [{
					ticks: {
						beginAtZero: true
					}
				}]
			},
		}
});
