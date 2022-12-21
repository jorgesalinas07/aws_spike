import re
from get_version import get_version
from markdown_to_text import parse_markdown_to_text, markdown_to_text

changelog_lines = {}
changelog_first_line = "v"+get_version("setup.py")
# changelog_first_line = f"## {os.getenv('NEW_VERSION')}"
# changelog_last_line = f"## {os.getenv('OLD_VERSION')}"
in_changelog_section = False
version_regex = '^v[0-9]\.+[0-9]+\.[0-9] \([^)]*\)'
changelog_line_regex = re.compile('^- (OFI-[1-9][0-9]*): (.*) \((#[1-9][0-9]*)\) \(([0-9a-f]+)\)$')
current_type = None

with open('CHANGELOG.md') as changelog_file:
    for line in changelog_file:
      text_line=markdown_to_text(line)
      print(text_line)
      if re.match(version_regex, text_line):
        if text_line.startswith(changelog_first_line):
          changelog_lines["version"]=text_line
          print(changelog_lines)
          continue
        break
      if text_line in ['Feature', 'Fix', 'Build', 'CI', 'DOCS', 'PERF', 'REFACTOR', 'TEST']:
        changelog_lines["type"]=text_line
        print(changelog_lines)
      continue
#print(parse_markdown_to_text("CHANGELOG.md"))
# parsed_changelog = parse_markdown_to_text("CHANGELOG.md")
# print(parsed_changelog)
# for line in parsed_changelog:
#   if line == "None":
#     print(line)
#   if version_regex.match(line):
#     if line.startswith(changelog_first_line):
#       print("Entro")
#       in_changelog_section = True
    
#     elif line.startswith(changelog_last_line):
#       in_changelog_section = False
#     elif in_changelog_section:
#       if line in ['Feature', 'Fix']:
#         current_type = line
#         continue
#       else:
#         parsed = changelog_line_regex.match(line)
#         changelog_lines.append({"type": current_type, "ticket": parsed.group(1), "title": parsed.group(2), "pr": parsed.group(3), "commit": parsed.group(4)})

# # slack_message = """
# # Released **{version}** to **{environment}**:
# # """.format(version=os.getenv('NEW_VERSION'), environment=os.getenv('ENVIRONMENT', 'Staging'))
# slack_message = """
# Released **{version}** to **{environment}**:
# """.format(version=changelog_first_line, environment='Staging')
# print(changelog_lines)
# for changelog_line in changelog_lines:
#   slack_message += f"- {changelog_line['ticket']}: {changelog_line['message']} ({changelog_line['pr']} merged as {changelog_line['commit']}) ({changelog_line['type']})"
# print(slack_message)
# # POST slack_message to Slack

# # Released v0.18.0 to Staging:
# # OFI-123: Release Engineering Implementation (#234 merged as abcdef123) (Feature)