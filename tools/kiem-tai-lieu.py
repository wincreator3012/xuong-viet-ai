#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""KIỂM TÀI LIỆU: tài liệu, skill và công cụ của xưởng (hay bản vẽ) còn khớp nhau.

    python3 tools/kiem-tai-lieu.py

Kiểm:
  1. Mỗi skills/<tên>/SKILL.md có phần đầu YAML, name trùng tên thư mục, mô tả tối đa 1024 ký tự, không có dấu < >;
     có kem.json với moTaNgan tối đa 200 ký tự; tệp trong "kem" có thật; tệp trong "chup" có thật hoặc có bản .mau.
  2. Đường dẫn trong dấu huyền ở các tệp .md (skills/..., chuan/..., tools/..., khuon/..., phong-cach/..., docs/...,
     mau-xuong/...; references/... trong cùng skill) trỏ tới tệp có thật.
  3. Bảng skill trong CLAUDE.md của xưởng (ở bản vẽ: mau-xuong/CLAUDE.md) nhắc đủ mọi skill.
  4. Mọi công cụ Python biên dịch được.
"""
import sys
sys.dont_write_bytecode = True
import json  # noqa: E402
import os  # noqa: E402
import re  # noqa: E402

import chung  # noqa: E402

GOC_DUONG = ('skills/', 'chuan/', 'tools/', 'khuon/', 'phong-cach/', 'docs/', 'mau-xuong/')
BO_QUA_THU_MUC = {'.git', '__pycache__', 'dong-goi', 'node_modules'}


def co_that(rel):
    p = os.path.join(chung.GOC, rel)
    if os.path.exists(p):
        return True
    if rel.startswith('phong-cach/') and rel.endswith('.md'):
        return os.path.exists(p[:-3] + '.mau.md')
    return False


def kiem_skill(loi):
    for ten in sorted(os.listdir(os.path.join(chung.GOC, 'skills'))):
        thu_muc = os.path.join(chung.GOC, 'skills', ten)
        if ten.startswith(('_', '.')) or not os.path.isdir(thu_muc):
            continue
        p = os.path.join(thu_muc, 'SKILL.md')
        if not os.path.exists(p):
            loi.append(f'skills/{ten}: thiếu SKILL.md')
            continue
        s = open(p, encoding='utf-8').read()
        m = re.match(r'^---\n(.*?)\n---\n', s, re.S)
        if not m:
            loi.append(f'skills/{ten}/SKILL.md: thiếu phần đầu YAML')
            continue
        fm = m.group(1)
        mt = re.search(r'^name:\s*(\S+)\s*$', fm, re.M)
        if not mt or mt.group(1) != ten:
            loi.append(f'skills/{ten}/SKILL.md: name phải là "{ten}"')
        md = re.search(r'^description:\s*(.*?)(?=^\w[\w-]*:|\Z)', fm, re.M | re.S)
        mo_ta = md.group(1).strip().lstrip('|>').strip().strip('"') if md else ''
        mo_ta = ' '.join(mo_ta.split())
        if not mo_ta or len(mo_ta) > 1024 or '<' in mo_ta or '>' in mo_ta:
            loi.append(f'skills/{ten}/SKILL.md: mô tả trống, quá 1024 ký tự ({len(mo_ta)}), hoặc có dấu < >')
        pk = os.path.join(thu_muc, 'kem.json')
        if not os.path.exists(pk):
            loi.append(f'skills/{ten}: thiếu kem.json')
            continue
        kem = json.load(open(pk, encoding='utf-8'))
        mtn = kem.get('moTaNgan', '')
        if not mtn or len(mtn) > 200 or '<' in mtn or '>' in mtn:
            loi.append(f'skills/{ten}/kem.json: moTaNgan trống, quá 200 ký tự ({len(mtn)}), hoặc có dấu < >')
        for nhom in ('kem', 'chup'):
            for dich, nguon in kem.get(nhom, {}).items():
                if not co_that(nguon.rstrip('/')):
                    loi.append(f'skills/{ten}/kem.json: {nhom} trỏ tới {nguon} không có')


def kiem_duong_dan(loi):
    for dp, dn, fn in os.walk(chung.GOC):
        dn[:] = [d for d in dn if d not in BO_QUA_THU_MUC and not d.startswith('.')]
        for f in fn:
            if not f.endswith('.md'):
                continue
            p = os.path.join(dp, f)
            rel_tep = os.path.relpath(p, chung.GOC).replace(os.sep, '/')
            if rel_tep.startswith('khuon/'):
                continue  # khuôn nói về thư mục của người dùng, không phải của xưởng
            skill = rel_tep.split('/')[1] if rel_tep.startswith('skills/') and rel_tep.count('/') >= 2 else None
            for so, dong in enumerate(open(p, encoding='utf-8').read().splitlines(), 1):
                for d in re.findall(r'`([^`\s]+)`', dong):
                    d = d.rstrip(':,.;)')
                    if any(k in d for k in ('<', '>', '*', '{', '[', '...')):
                        continue
                    if d.startswith(GOC_DUONG) and '.' in d.rsplit('/', 1)[-1]:
                        if not co_that(d):
                            loi.append(f'{rel_tep}:{so}: `{d}` không có')
                    elif skill and d.startswith('references/') and d.endswith('.md'):
                        if not os.path.exists(os.path.join(chung.GOC, 'skills', skill, d)) \
                                and d not in ('references/GIONG-VAN.md', 'references/DONG-GOI.md',
                                              'references/bai-hoc-giong.md', 'references/ho-so-nguoi-viet.md'):
                            loi.append(f'{rel_tep}:{so}: `{d}` không có trong skills/{skill}/')


def kiem_bang_skill(loi):
    p = os.path.join(chung.GOC, 'CLAUDE.md' if chung.la_xuong() else 'mau-xuong/CLAUDE.md')
    if not os.path.exists(p):
        loi.append(f'thiếu {os.path.relpath(p, chung.GOC)}')
        return
    s = open(p, encoding='utf-8').read()
    for ten in sorted(os.listdir(os.path.join(chung.GOC, 'skills'))):
        if not ten.startswith(('_', '.')) and os.path.isdir(os.path.join(chung.GOC, 'skills', ten)) \
                and f'skills/{ten}/' not in s:
            loi.append(f'{os.path.relpath(p, chung.GOC)}: bảng skill chưa nhắc skills/{ten}/')


def kiem_cong_cu(loi):
    for f in sorted(os.listdir(os.path.join(chung.GOC, 'tools'))):
        if f.endswith('.py'):
            p = os.path.join(chung.GOC, 'tools', f)
            try:
                compile(open(p, encoding='utf-8').read(), p, 'exec')
            except SyntaxError as e:
                loi.append(f'tools/{f}: lỗi cú pháp dòng {e.lineno}')


def main():
    loi = []
    kiem_skill(loi)
    kiem_duong_dan(loi)
    kiem_bang_skill(loi)
    kiem_cong_cu(loi)
    for l in loi:
        print('  LỖI: ' + l)
    print(f'\nKIỂM TÀI LIỆU: ' + ('ĐẠT' if not loi else f'KHÔNG ĐẠT ({len(loi)} lỗi)'))
    sys.exit(0 if not loi else 1)


if __name__ == '__main__':
    main()
