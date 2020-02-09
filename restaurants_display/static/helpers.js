function display(restaurants)
{
    for ( r of restaurants){
        var img = '<img src=' + r.image + ' style="width:20%;height:30%";>';
        var content = '<div class="restaurant">' + '<p>' + r.name + '</p>'
            + '<p>' + r.description + '</p>'  + img + '</div> <br>';
        $('#list').append(content);
    }
}

function sort(restaurants) {
    var button = $("#sort");

    button.click(function() {
        var value = parseInt(button.val());
        // console.log(value);
        if (value === 0 || value === -1){
            // in ascending order
            restaurants.sort(compareValues('name'));
            button.val(1);
        }
        else if (value === 1){
            // in descending order
            restaurants.sort(compareValues('name', 'desc'));
            button.val(-1);
        }
        else{
            alert("Error!")
        }

        $("#list").empty();
        display(restaurants);
        // Get the elements with class="column"
var elements = document.getElementsByClassName("columns");
console.log(elements.length);

    });
}


function compareValues(key, order = 'asc') {
  return function innerSort(a, b) {
    if (!a.hasOwnProperty(key) || !b.hasOwnProperty(key)) {
      // property doesn't exist on either object
      return 0;
    }

    const varA = (typeof a[key] === 'string')
      ? a[key].toUpperCase() : a[key];
    const varB = (typeof b[key] === 'string')
      ? b[key].toUpperCase() : b[key];

    let comparison = 0;
    if (varA > varB) {
      comparison = 1;
    } else if (varA < varB) {
      comparison = -1;
    }
    return (
      (order === 'desc') ? (comparison * -1) : comparison
    );
  };
}