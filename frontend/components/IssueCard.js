export default function IssueCard({ issue }) {
  return (
    <div className="border p-4 rounded-lg shadow-md">
      <h3 className="text-lg font-bold">{issue.title}</h3>
      <p className="text-sm mt-2">{issue.summary}</p>
      <a href={issue.url} target="_blank" rel="noopener noreferrer" className="text-blue-600 mt-3 inline-block">View on GitHub</a>
    </div>
  );
}
