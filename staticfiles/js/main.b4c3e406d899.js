function init(){
 alert('all set')
}

function getExams(){
  
  const exam_url='http://127.0.0.1:8000/api/exams/'
  fetch(exam_url)
  .then(request=>request.json())
  .then(data=>{
    let str_html=''
    facid = document.getElementById('facid').value
    data.forEach(element =>{
      str_html +=element.exam + ' - ' + element.startdate + '<hr/>'
    })
  document.getElementById('idExams').innerHTML=str_html
 })
}


function saveExams() {
  const exam = document.getElementById('exam').value;
  const startdate = document.getElementById('startdate').value;
  const enddate = document.getElementById('enddate').value;
  const faculty = document.getElementById('facid').value;
  const exam_url = 'http://127.0.0.1:8000/api/exams/'

  fetch(exam_url, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      exam: exam,
      startdate: startdate,
      enddate: enddate,
      faculty: faculty,
    })
  })
  .then(response => response.json())
  .then(data => {
    console.log(data);
    getExams();
  })
  .catch(error => console.error('Error:', error));
}


function getStudents() {
  fetch('http://127.0.0.1:8000/api/students/')
    .then(res => res.json())
    .then(data => {
      const studentList = document.getElementById('studentList');
      studentList.innerHTML = '';
      
      data.forEach(student => {
        studentList.innerHTML += `<p>ID: ${student.id} | Name: ${student.name} | Programe : ${student.prog}</p>`;
      });
    })
    .catch(err => console.error('Error fetching students:', err));
}

function getCSRFToken() {
    return document.querySelector('meta[name="csrf-token"]').content;
}

function addStudent() {
  const name = document.getElementById('name').value;
  // const unm = document.getElementById('unm').value;
  const pwd = document.getElementById('pwd').value;
  const prog = document.getElementById('prog').value;
  if (!name) {
    alert('Please enter a name');
    return;
  }

  fetch('http://127.0.0.1:8000/api/students/', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'X-CSRFToken': getCSRFToken(),
    },
    body: JSON.stringify({ 
      name:name,
      // unm:unm,
      pwd:pwd,
      prog:prog
     })
  })
    .then(res => res.json())
    .then(data => {
      console.log('Student added:', data);
      document.getElementById('name').value = '';
      getStudents();
    })
    .catch(err => console.error('Error adding student:', err));
}

function getExamQuestions() {
  fetch('http://127.0.0.1:8000/api/exams/')
    .then(res => res.json())
    .then(data => {
      const examSelect = document.getElementById('examSelect');
      data.forEach(exam => {
        const option = document.createElement('option');
        option.value = exam.id;
        option.text = `${exam.exam} (${exam.startdate} - ${exam.enddate})`;
        examSelect.appendChild(option);
      });
    });
}

function saveQuestions() {
  const que = document.getElementById('queText').value;
  const marks = document.getElementById('marks').value;
  const examId = document.getElementById('examSelect').value;

  if (!que || !marks || !examId) {
    alert("Please fill in all fields");
    return;
  }

  fetch('http://127.0.0.1:8000/api/questions/', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      que: que,
      marks: parseInt(marks),
      exam: examId
    })
  })
    .then(res => res.json())
    .then(data => {
      console.log('Question saved:', data);
      getQuestions(); // Refresh
    })
    .catch(err => console.error('Error:', err));
}

function getQuestions() {
  fetch('http://127.0.0.1:8000/api/questions/')
    .then(res => res.json())
    .then(data => {
      const list = document.getElementById('questionList');
      list.innerHTML = '';
      data.forEach(q => {
        list.innerHTML += `<p>${q.que} (Marks: ${q.marks}) - Exam ID: ${q.exam}</p><hr/>`;
      });
    });
}