function addTimeBlockRow() {
    var table = document.getElementById('time-blocks').getElementsByTagName('tbody')[0];
    var newRow = table.insertRow(table.rows.length);

    var timeCell = newRow.insertCell(0);
    var taskCell = newRow.insertCell(1);

    timeCell.innerHTML = '<input type="time" required> - <input type="time" required>';
    taskCell.innerHTML = '<textarea rows="2" cols="20" required></textarea>';
}
