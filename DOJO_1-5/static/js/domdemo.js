var timezones;
fetch("static/timezones.json").then((response) => response.json()).then((data) => {
    timezones = data;
});
document.addEventListener("DOMContentLoaded", (event) => {
    let update_interval = setInterval(update_time, 1000);
    let clock_holder = document.querySelector('#clock_holder');
    let num_clocks = 0;
    let indices = [];

    document.querySelector('#add').addEventListener("submit", (event) => {
       event.preventDefault();
       let input = event.target.querySelector(`input[type='text']`).value;
       if(timezones.hasOwnProperty(input.toUpperCase())) {
           add_clock(input.toUpperCase());
       } else {
           alert('wrong');
       }

       event.target.reset();
    });

    document.querySelector('#remove').addEventListener('submit', (event) => {
       event.preventDefault();
       let input = parseInt(event.target.querySelector(`input[type='number']`).value, 10);
       if(input >= 0 && input < indices.length) {
           remove_clock(input);
       } else {
           alert('Invalid clock!');
       }
       event.target.reset();
    });

    function add_clock(timezone) {
        let new_clock = document.querySelector('template').content.cloneNode(true);
        num_clocks++;
        new_clock.querySelector('strong').innerText = timezone;
        new_clock.querySelector('strong').setAttribute('data-offset', timezones[timezone]);
        new_clock.querySelector('article').id = `clock${num_clocks}`;
        indices.push(num_clocks);
        let date = new Date;
        new_clock.querySelector('time').innerText = (date.toLocaleTimeString());
        clock_holder.appendChild(new_clock);
    };

    function remove_clock(index) {
        let clock_number = indices[index];
        document.querySelector('#clock_holder').removeChild(document.querySelector(`#clock${clock_number}`));
        indices.splice(index, 1);
        num_clocks--;
    };

    function update_time() {
        let clocks = document.querySelectorAll('.clock');
        clocks.forEach((x) => {
            let timezone_offset = x.querySelector('strong').innerText;
            x.querySelector('time').innerText = getTime(timezone_offset);
        });
    }

    function getTime(timezone) {
        let options = {
                timeZone: timezone,
                hour: 'numeric',
                minute: 'numeric',
                second: 'numeric',
            },
            formatter = new Intl.DateTimeFormat([], options);
        return formatter.format(new Date());
    }
});