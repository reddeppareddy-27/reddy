// Handle state dropdown change
$('#state').change(function () {
    const stateId = $(this).val();
    if (stateId) {
        // Fetch districts for the selected state
        $.get('/get-districts/', { state_id: stateId }, function (data) {
            const districts = data.districts;
            $('#district').html('<option value="">--Select District--</option>');
            districts.forEach(d => {
                $('#district').append(`<option value="${d.id}">${d.name}</option>`);
            });
            $('#district').prop('disabled', false);
        }).fail(function () {
            alert("Error fetching districts. Please try again.");
        });
    } else {
        // Reset dependent dropdowns
        $('#district').prop('disabled', true).html('<option value="">--Select District--</option>');
        $('#city').prop('disabled', true).html('<option value="">--Select City--</option>');
        $('#gyms-list').empty();
    }
});

// Handle district dropdown change
$('#district').change(function () {
    const districtId = $(this).val();
    if (districtId) {
        // Fetch cities for the selected district
        $.get('/get-cities/', { district_id: districtId }, function (data) {
            const cities = data.cities;
            $('#city').html('<option value="">--Select City--</option>');
            cities.forEach(c => {
                $('#city').append(`<option value="${c.id}">${c.name}</option>`);
            });
            $('#city').prop('disabled', false);
        }).fail(function () {
            alert("Error fetching cities. Please try again.");
        });
    } else {
        // Reset city dropdown
        $('#city').prop('disabled', true).html('<option value="">--Select City--</option>');
        $('#gyms-list').empty();
    }
});

// Handle city dropdown change
$('#city').change(function () {
    const cityId = $(this).val();
    if (cityId) {
        // Fetch gyms for the selected city
        $.get('/get-gyms/', { city_id: cityId }, function (data) {
            const gyms = data.gyms;
            $('#gyms-list').empty(); // Clear the gym list
            gyms.forEach(g => {
                $('#gyms-list').append(`
                    <li class="gym-item">
                        <div class="gym-image-container">
                            ${g.image ? `<img src="${g.image}" alt="${g.name}" class="gym-image" />` : '<p>No image available</p>'}
                        </div>
                        <div class="gym-details">
                            <h3>${g.name}</h3>
                            <p>Phone: ${g.phone_number}</p>
                            <a href="${g.google_maps_link}" target="_blank">Location Link</a>
                        </div>
                    </li>
                `);
            });
        }).fail(function () {
            alert("Error fetching gyms. Please try again.");
        });
    } else {
        $('#gyms-list').empty(); // Clear the gym list if no city is selected
    }
});
