from chimerax.core.commands import run
run(session, 'open 6U0K')
run(session, 'show c')
run(session, 'show a')
run(session, 'style stick')
run(session, 'transparency 50 atoms')
run(session, 'color bychain')
run(session, 'color byhetero')
run(session, 'cartoon style modeHelix tube sides 20')
run(session, 'sequence chain all')
run(session, 'view orient')
run(session, 'ui tool show "Side View"')
run(session, 'graphics silhouettes true')
run(session, 'set bgColor #ffffff00')