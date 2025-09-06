import { useState, useEffect } from "react";
import axios from "axios";
import IssueCard from "../components/IssueCard";

export default function Dashboard() {
const [issues, setIssues] = useState([]);

useEffect(() => {
  fetch("http://127.0.0.1:8000/issues")
    .then(res => res.json())
    .then(data => setIssues(data))
    .catch(err => console.error("Error fetching issues:", err));
}, []);



  return (
    <div className="p-6">
      <h2 className="text-2xl font-semibold mb-4">Good First Issues</h2>
      <div className="grid gap-4">
        {issues.map((issue, idx) => (
          <IssueCard key={idx} issue={issue} />
        ))}
      </div>
    </div>
  )
}
