let ChartOne = document.getElementById('ChartOne').getContext("2d");

let barChart = new Chart(ChartOne, {

  type : 'doughnut', // pie, line, doughnut, polarArea
  data : {
    labels : ['positive', 'negative', 'neutral'],
    datasets : [
      {
        label : 'peoples think',
        data:[10, 20, 30],
        backgroundColor: [
  					'#251D3A',
  					'#2A2550',
  					'#E04D01',
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
