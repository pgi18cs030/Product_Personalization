function myFunction() {
  var checkBox = document.getElementById("cc");
  var checkBox1 = document.getElementById("sc");
  var checkBox2 = document.getElementById("ss");
  var checkBox3 = document.getElementById("pp");
  var text = document.getElementById("text");
  var text1 = document.getElementById("text1");
  var text2 = document.getElementById("text2");
  var text3 = document.getElementById("text3");
  if (checkBox.checked == true){

    text.style.display = "block";
  } else {
     text.style.display = "none";
  }
  if (checkBox1.checked == true){

    text1.style.display = "block";
  } else {
     text1.style.display = "none";
  }
  if (checkBox2.checked == true){

    text2.style.display = "block";
  } else {
     text2.style.display = "none";
  }
  if (checkBox3.checked == true){

    text3.style.display = "block";
  } else {
     text3.style.display = "none";
  }
}

function anyCheckbox()
{
    var inputElements = document.querySelectorAll('input[name="brand"]:checked');


    for (var i = 0; i < inputElements.length; i++)
    {
        if (inputElements[i].type == "checkbox")
            if (inputElements[i].checked){
                   console.log(inputElements[i])
                   var text = document.getElementById(inputElements[i].value+"data1");
                   var text1 = document.getElementById(inputElements[i].value+"data1");
                   var text2 = document.getElementById(inputElements[i].value+"data1");
                   var text3 = document.getElementById(inputElements[i].value+"data1");

                   text.style.display="block";
                   text1.style.display="block";
                   text2.style.display="block";
                   text3.style.display="block";
            }
            else
            {
                text.style.display="none";
                text1.style.display="none";
                text2.style.display="none";
                text3.style.display="none";
            }


}

}
