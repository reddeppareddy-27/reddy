// Event Listener for State Selection
document.getElementById('state-select').addEventListener('change', function () {
    const stateId = this.value;
    const districtSelect = document.getElementById('district-select');
    const locationSelect = document.getElementById('location-select');
    const gymsList = document.getElementById('gyms-list');

    // Reset District, Location, and Gyms Dropdowns
    districtSelect.innerHTML = '<option value="">-- Select District --</option>';
    districtSelect.disabled = true;
    locationSelect.innerHTML = '<option value="">-- Select Location --</option>';
    locationSelect.disabled = true;
    gymsList.innerHTML = '';

    // Fetch Districts for the Selected State
    if (stateId) {
        fetch(`/districts/${stateId}/`)
            .then(response => {
                if (!response.ok) {
                    throw new Error('Failed to fetch districts');
                }
                return response.json();
            })
            .then(data => {
                data.forEach(district => {
                    const option = document.createElement('option');
                    option.value = district.id;
                    option.textContent = district.name;
                    districtSelect.appendChild(option);
                });
                districtSelect.disabled = false; // Enable District Dropdown
            })
            .catch(error => {
                console.error('Error fetching districts:', error);
                alert('Failed to load districts. Please try again later.');
            });
    }
});

// Event Listener for District Selection
document.getElementById('district-select').addEventListener('change', function () {
    const districtId = this.value;
    const locationSelect = document.getElementById('location-select');
    const gymsList = document.getElementById('gyms-list');

    // Reset Location and Gyms Dropdowns
    locationSelect.innerHTML = '<option value="">-- Select Location --</option>';
    locationSelect.disabled = true;
    gymsList.innerHTML = '';

    // Fetch Locations for the Selected District
    if (districtId) {
        fetch(`/locations/${districtId}/`)
            .then(response => {
                if (!response.ok) {
                    throw new Error('Failed to fetch locations');
                }
                return response.json();
            })
            .then(data => {
                data.forEach(location => {
                    const option = document.createElement('option');
                    option.value = location.id;
                    option.textContent = location.name;
                    locationSelect.appendChild(option);
                });
                locationSelect.disabled = false; // Enable Location Dropdown
            })
            .catch(error => {
                console.error('Error fetching locations:', error);
                alert('Failed to load locations. Please try again later.');
            });
    }
});

// Event Listener for Location Selection
document.getElementById('location-select').addEventListener('change', function () {
    const locationId = this.value;
    const gymsList = document.getElementById('gyms-list');

    // Reset Gyms List
    gymsList.innerHTML = '';

    // Fetch Gyms for the Selected Location
    if (locationId) {
        fetch(`/gyms/${locationId}/`)
            .then(response => {
                if (!response.ok) {
                    throw new Error('Failed to fetch gyms');
                }
                return response.json();
            })
            .then(data => {
                data.forEach(gym => {
                    const li = document.createElement('li');
                    li.textContent = gym.name;
                    gymsList.appendChild(li);
                });
            })
            .catch(error => {
                console.error('Error fetching gyms:', error);
                alert('Failed to load gyms. Please try again later.');
            });
    }
});
