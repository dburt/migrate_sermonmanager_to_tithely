import json
import click

def handle_output(data, output_path):
    """Handles outputting data to a file or stdout."""
    if output_path:
        if output_path == "stdout":
            click.echo(json.dumps(data, indent=4))
        else:
            with open(output_path, 'w') as f:
                json.dump(data, f, indent=4)
            click.echo(f"Saved {len(data)} items to {output_path}")
    else:
        if isinstance(data, list):
            for item in data:
                click.echo(f"- {item.get('title', item)}")
        else:
            click.echo(data)
