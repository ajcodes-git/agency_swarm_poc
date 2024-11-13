from agency_swarm.tools import BaseTool
from pydantic import Field

class PenetrationTestingPlanTool(BaseTool):
    """
    A tool to outline the 5-step penetration testing plan for a specified organization.
    This tool will help in creating a structured plan for conducting penetration tests,
    detailing the approach for each stage based on industry-standard methodologies.
    """
    organization_name: str = Field(..., description="The name of the organization to be tested")

    def run(self):
        """
        Generates a 5-step penetration testing plan for the specified organization.
        The plan includes Reconnaissance, Scanning, Gaining Access, Maintaining Access, and Covering Tracks.
        """
        steps = [
            {
                "Step": "Reconnaissance",
                "Description": (
                    f"Gather public and private information about {self.organization_name} to identify potential "
                    "attack vectors. Techniques may include OSINT, domain enumeration, and social engineering."
                ),
            },
            {
                "Step": "Scanning",
                "Description": (
                    f"Perform scans on {self.organization_name}'s network and applications to identify open ports, "
                    "services, and vulnerabilities. Use tools like Nmap, Nessus, or OpenVAS for vulnerability scanning."
                ),
            },
            {
                "Step": "Gaining Access",
                "Description": (
                    f"Attempt to exploit identified vulnerabilities within {self.organization_name}'s systems to gain "
                    "access. Techniques may include SQL injection, phishing, password attacks, or exploiting application "
                    "vulnerabilities."
                ),
            },
            {
                "Step": "Maintaining Access",
                "Description": (
                    f"Establish a backdoor or persistence mechanism in {self.organization_name}'s systems to ensure "
                    "continuous access. This can be done by creating user accounts, installing remote access tools, "
                    "or leveraging vulnerabilities for long-term access."
                ),
            },
            {
                "Step": "Covering Tracks",
                "Description": (
                    f"Remove any signs of the penetration testing activities on {self.organization_name}'s systems, "
                    "such as logs or traces of access. This step is critical to simulate the actions of a real threat actor "
                    "who would attempt to avoid detection."
                ),
            },
        ]

        return {
            "organization": self.organization_name,
            "penetration_testing_plan": steps
        }

# Test tool
if __name__ == "__main__":
    tool = PenetrationTestingPlanTool(organization_name="Acme Corp")
    result = tool.run()
    for step in result["penetration_testing_plan"]:
        print(f"{step['Step']}: {step['Description']}")
