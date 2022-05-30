let ChartOne = document.getElementById('ChartOne').getContext("2d");

let barChart = new Chart(ChartOne, {

  type : 'doughnut', // pie, line, doughnut, polarArea
  data : {
    labels : ['positive', 'negative', 'haha'],
    datasets : [
      {
        label : 'peoples think',
        data:[10, 20, 30],
        backgroundColor:['red', 'blue']
    }]
}
})
