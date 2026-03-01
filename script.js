let assignments = [];
let totalStudyHours = 0;
function addAssignment() 
{
    const title = document.getElementById("title").value;
    const subject = document.getElementById("subject").value;
    const dueDate = document.getElementById("dueDate").value;
    if (title === "" || subject === "" || dueDate === "") 
        {
        alert("Please fill all fields");
        return;
    }
    const assignment = {
        title: title,
        subject: subject,
        dueDate: dueDate,
        completed: false
    };
    assignments.push(assignment);
    displayAssignments();
    document.getElementById("title").value = "";
    document.getElementById("subject").value = "";
    document.getElementById("dueDate").value = "";
}
function displayAssignments() 
{
    const list = document.getElementById("assignmentList");
    list.innerHTML = "";
    assignments.forEach((assignment, index) => 
        {
        const li = document.createElement("li");
        li.innerHTML = `
            ${assignment.title} (${assignment.subject}) - Due: ${assignment.dueDate}
            <button onclick="markCompleted(${index})">Complete</button>
        `;
        list.appendChild(li);
    });
}
function markCompleted(index) 
{
    assignments.splice(index, 1);
    displayAssignments();
}
function logHours() 
{
    const hours = parseFloat(document.getElementById("hours").value);
    if (isNaN(hours) || hours <= 0) 
        {
        alert("Enter valid hours");
        return;
    }
    totalStudyHours += hours;
    document.getElementById("totalHours").innerText =
        "Total Study Hours: " + totalStudyHours;
    document.getElementById("hours").value = "";
}