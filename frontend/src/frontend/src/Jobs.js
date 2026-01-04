import { useEffect, useState } from "react";

export default function Jobs() {
  const [jobs, setJobs] = useState([]);

  useEffect(() => {
    fetch("http://localhost:8000/jobs")
      .then(res => res.json())
      .then(data => setJobs(data));
  }, []);

  return (
    <ul>
      {jobs.map((j, i) => <li key={i}>{j.title}</li>)}
    </ul>
  );
}
