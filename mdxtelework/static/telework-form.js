//function addTimeBlockRow() {
   // var table = document.getElementById('time-blocks').getElementsByTagName('tbody')[0];
   // var newRow = table.insertRow(table.rows.length);

   // var timeCell = newRow.insertCell(0);
   // var taskCell = newRow.insertCell(1);

  //  timeCell.innerHTML = '<input type="time" name="time-block-1" required> - <input type="time" name="time-block-2" required>';
   // taskCell.innerHTML = '<textarea name="task-break" rows="2" cols="20" required></textarea>';
//}


function addTimeBlockRow() {
    var table = document.getElementById('time-blocks').getElementsByTagName('tbody')[0];
    var newRow = table.insertRow(table.rows.length);

    var startTimeCell = newRow.insertCell(0);
    var endTimeCell = newRow.insertCell(1);
    var activityCell = newRow.insertCell(2);
    var removeCell = newRow.insertCell(3); // New cell for Remove button

    startTimeCell.innerHTML = '<input type="time" name="start-time" required>';
    endTimeCell.innerHTML = '<input type="time" name="end-time" required>';
    activityCell.innerHTML = '<input type="text" name="activity" required>';
    removeCell.innerHTML = '<button type="button" onclick="removeTimeBlockRow(this)">Remove</button>'; // Button to remove row
}

function removeTimeBlockRow(button) {
    var row = button.parentNode.parentNode; // Get the row containing the button
    row.parentNode.removeChild(row); // Remove the row
}
