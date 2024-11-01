# Tau Tubulin Kinase 1 for Alzheimer's research

from chimerax.core.commands import run
run(session, 'open 7JXY')
run(session, 'show c')
run(session, 'show a')
run(session, 'show surfaces')
run(session, 'color sequential palette Purples-5')
run(session, 'style ball')
run(session, 'transparency 90 surfaces')
run(session, 'sequence chain /A /B')
run(session, 'view orient')
run(session, 'ui tool show "Side View"')
run(session, 'graphics silhouettes true')
run(session, 'set bgColor #ffffff00')
