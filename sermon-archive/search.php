<?php
/**
 * Server-side full-text search over sermons, including transcript contents.
 *
 * Queries the read-only search.db (an FTS5 index, rebuilt by `export`) and
 * returns matching sermon slugs so the static page can join against sermons.json.
 *
 * GET /search.php?q=...&limit=...
 *  -> {"query": "...", "count": N, "results": [{"slug": "...", "sermon_key": 123, "rank": 1.2}]}
 */

header('Content-Type: application/json; charset=utf-8');
// Search results are dynamic; never let Apache's default expiry cache them.
header('Cache-Control: no-store, max-age=0');

$q = isset($_GET['q']) ? trim((string) $_GET['q']) : '';
$limit = isset($_GET['limit']) ? max(1, min(200, (int) $_GET['limit'])) : 60;

if ($q === '') {
    echo json_encode(['query' => $q, 'count' => 0, 'results' => []]);
    exit;
}

// Build a safe FTS5 query: tokenize, strip operators/special chars, prefix-match each term.
$tokens = preg_split('/\s+/', $q);
$terms = [];
foreach ($tokens as $t) {
    $t = preg_replace('/[^a-zA-Z0-9]/', '', $t);
    if ($t !== '') {
        $terms[] = '"' . $t . '"*';
    }
}

if (empty($terms)) {
    echo json_encode(['query' => $q, 'count' => 0, 'results' => []]);
    exit;
}
$fts = implode(' AND ', $terms);

try {
    $db = new PDO('sqlite:' . __DIR__ . '/search.db');
    $db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    $stmt = $db->prepare(
        'SELECT slug, sermon_key, rank FROM sermons_fts
         WHERE sermons_fts MATCH :q ORDER BY rank LIMIT :lim'
    );
    $stmt->bindValue(':q', $fts, PDO::PARAM_STR);
    $stmt->bindValue(':lim', $limit, PDO::PARAM_INT);
    $stmt->execute();
    $results = $stmt->fetchAll(PDO::FETCH_ASSOC);
    foreach ($results as &$r) {
        $r['rank'] = round((float) $r['rank'], 4);
    }
    echo json_encode(['query' => $q, 'count' => count($results), 'results' => $results]);
} catch (Exception $e) {
    http_response_code(500);
    echo json_encode(['error' => 'search unavailable']);
}