/* function to create html content string in tooltip div. */
function tooltipHtml(n, d){	
  return "<h4>"+n+"</h4><table>" +
    "<tr><td>Average</td><td>$" + (d.avg) + "K</td></tr>" +
    "</table>"
}

var sampleData = {}
var state_data = []

d3.csv("data/state_data.csv", function(data) {
  state_data = data
  for (var e in state_data){
    var z = state_data[e]
    var i = z["id"]
    var s = z["Salary"] 
    sampleData[i]={id:i, avg:s, color:d3.interpolate("steelblue","black")((s -70)/100)}
  }

  uStates.draw("#statesvg", sampleData, tooltipHtml)
})
