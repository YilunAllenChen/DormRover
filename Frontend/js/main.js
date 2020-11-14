



document.getElementsByName("speed"); // returns a list of elements with name="textbox1"
// document.getElementsByName("speed")[0] // returns the first element in DOM with name="textbox1"




async function send_key(key)
{
    let response = await fetch
    (window.location.href + 'command', 
        {
                  method: 'POST',
                  headers: {
                      'Content-Type': 'application/json',
                  },
                  body: JSON.stringify({
                    "key" : key
                  })
        }
    )
    return response
  }

/*

  function processForm() 
	  { 
		var parameters = location.search //.substring(1).split("&"); 
		var temp = parameters[0] //.split("="); 
		x = unescape(temp[1]); 
	    document.getElementById('temp').innerHTML=x; 
      } 
    processForm(); 


async function get_data(sensortype)
  {
    let response = fetch
    (window.location.href + 'get_sensor_data',
        {
                  method: 'GET',
                  headers: {
                      'Content-Type': 'application/json',
                  },
                  body: JSON.stringify({
                    "key" : sensortype
                  })
        }
    )   
    return response.json
  }




async function fetch(window.location.href + 'get_sensor_data', {
    method: "GET",
    credentials: "include",
    body: JSON.stringify(entry),
    cache: "no-cache",
    headers: new Headers({
      "content-type": "application/json"
    })
  })
  .then(function(response) {
    if (response.status !== 200) {
      console.log(`Looks like there was a problem. Status code: ${response.status}`);
      return;
    }

    response.json().then(function(data) {
      console.log(data);
    });
  })
  .catch(function(error) {
    console.log("Fetch error: " + error);
});
*/






  forward.onclick = async (e) => {let res = await send_key('w');}
  

  backward.onclick = async (e) => {let res = await send_key('s');}

  left.onclick = async (e) => {let res = await send_key('a');}

  right.onclick = async (e) => {let res = await send_key('d');}

  //send keyboard event
  document.onkeydown = async (e) => {let res = await send_key(e);}






