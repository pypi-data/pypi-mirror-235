from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'eos/flow-tracking.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_flow_tracking = resolve('flow_tracking')
    try:
        t_1 = environment.tests['arista.avd.defined']
    except KeyError:
        @internalcode
        def t_1(*unused):
            raise TemplateRuntimeError("No test named 'arista.avd.defined' found.")
    pass
    if t_1(environment.getattr((undefined(name='flow_tracking') if l_0_flow_tracking is missing else l_0_flow_tracking), 'sampled')):
        pass
        yield '!\nflow tracking sampled\n'
        if t_1(environment.getattr(environment.getattr((undefined(name='flow_tracking') if l_0_flow_tracking is missing else l_0_flow_tracking), 'sampled'), 'sample')):
            pass
            yield '   sample '
            yield str(environment.getattr(environment.getattr((undefined(name='flow_tracking') if l_0_flow_tracking is missing else l_0_flow_tracking), 'sampled'), 'sample'))
            yield '\n'
        for l_1_tracker in environment.getattr(environment.getattr((undefined(name='flow_tracking') if l_0_flow_tracking is missing else l_0_flow_tracking), 'sampled'), 'trackers'):
            _loop_vars = {}
            pass
            yield '   tracker '
            yield str(environment.getattr(l_1_tracker, 'name'))
            yield '\n'
            if t_1(environment.getattr(environment.getattr(l_1_tracker, 'record_export'), 'on_inactive_timeout')):
                pass
                yield '      record export on inactive timeout '
                yield str(environment.getattr(environment.getattr(l_1_tracker, 'record_export'), 'on_inactive_timeout'))
                yield '\n'
            if t_1(environment.getattr(environment.getattr(l_1_tracker, 'record_export'), 'on_interval')):
                pass
                yield '      record export on interval '
                yield str(environment.getattr(environment.getattr(l_1_tracker, 'record_export'), 'on_interval'))
                yield '\n'
            if t_1(environment.getattr(environment.getattr(l_1_tracker, 'record_export'), 'mpls'), True):
                pass
                yield '      record export mpls\n'
            if t_1(environment.getattr(l_1_tracker, 'exporters')):
                pass
                for l_2_exporter in environment.getattr(l_1_tracker, 'exporters'):
                    l_2_collector_cli = resolve('collector_cli')
                    _loop_vars = {}
                    pass
                    yield '      exporter '
                    yield str(environment.getattr(l_2_exporter, 'name'))
                    yield '\n'
                    if t_1(environment.getattr(environment.getattr(l_2_exporter, 'collector'), 'host')):
                        pass
                        l_2_collector_cli = str_join(('collector ', environment.getattr(environment.getattr(l_2_exporter, 'collector'), 'host'), ))
                        _loop_vars['collector_cli'] = l_2_collector_cli
                        if t_1(environment.getattr(environment.getattr(l_2_exporter, 'collector'), 'port')):
                            pass
                            l_2_collector_cli = str_join(((undefined(name='collector_cli') if l_2_collector_cli is missing else l_2_collector_cli), ' port ', environment.getattr(environment.getattr(l_2_exporter, 'collector'), 'port'), ))
                            _loop_vars['collector_cli'] = l_2_collector_cli
                        yield '         '
                        yield str((undefined(name='collector_cli') if l_2_collector_cli is missing else l_2_collector_cli))
                        yield '\n'
                    if t_1(environment.getattr(environment.getattr(l_2_exporter, 'format'), 'ipfix_version')):
                        pass
                        yield '         format ipfix version '
                        yield str(environment.getattr(environment.getattr(l_2_exporter, 'format'), 'ipfix_version'))
                        yield '\n'
                    if t_1(environment.getattr(l_2_exporter, 'local_interface')):
                        pass
                        yield '         local interface '
                        yield str(environment.getattr(l_2_exporter, 'local_interface'))
                        yield '\n'
                    if t_1(environment.getattr(l_2_exporter, 'template_interval')):
                        pass
                        yield '         template interval '
                        yield str(environment.getattr(l_2_exporter, 'template_interval'))
                        yield '\n'
                l_2_exporter = l_2_collector_cli = missing
            if t_1(environment.getattr(l_1_tracker, 'table_size')):
                pass
                yield '      flow table size '
                yield str(environment.getattr(l_1_tracker, 'table_size'))
                yield ' entries\n'
        l_1_tracker = missing
        if t_1(environment.getattr(environment.getattr((undefined(name='flow_tracking') if l_0_flow_tracking is missing else l_0_flow_tracking), 'sampled'), 'shutdown'), False):
            pass
            yield '   no shutdown\n'
    if t_1(environment.getattr((undefined(name='flow_tracking') if l_0_flow_tracking is missing else l_0_flow_tracking), 'hardware')):
        pass
        yield '!\nflow tracking hardware\n'
        for l_1_tracker in environment.getattr(environment.getattr((undefined(name='flow_tracking') if l_0_flow_tracking is missing else l_0_flow_tracking), 'hardware'), 'trackers'):
            _loop_vars = {}
            pass
            yield '   tracker '
            yield str(environment.getattr(l_1_tracker, 'name'))
            yield '\n'
            if t_1(environment.getattr(environment.getattr(l_1_tracker, 'record_export'), 'on_inactive_timeout')):
                pass
                yield '      record export on inactive timeout '
                yield str(environment.getattr(environment.getattr(l_1_tracker, 'record_export'), 'on_inactive_timeout'))
                yield '\n'
            if t_1(environment.getattr(environment.getattr(l_1_tracker, 'record_export'), 'on_interval')):
                pass
                yield '      record export on interval '
                yield str(environment.getattr(environment.getattr(l_1_tracker, 'record_export'), 'on_interval'))
                yield '\n'
            if t_1(environment.getattr(environment.getattr(l_1_tracker, 'record_export'), 'mpls'), True):
                pass
                yield '      record export mpls\n'
            if t_1(environment.getattr(l_1_tracker, 'exporters')):
                pass
                for l_2_exporter in environment.getattr(l_1_tracker, 'exporters'):
                    l_2_collector_cli = resolve('collector_cli')
                    _loop_vars = {}
                    pass
                    yield '      exporter '
                    yield str(environment.getattr(l_2_exporter, 'name'))
                    yield '\n'
                    if t_1(environment.getattr(environment.getattr(l_2_exporter, 'collector'), 'host')):
                        pass
                        l_2_collector_cli = str_join(('collector ', environment.getattr(environment.getattr(l_2_exporter, 'collector'), 'host'), ))
                        _loop_vars['collector_cli'] = l_2_collector_cli
                        if t_1(environment.getattr(environment.getattr(l_2_exporter, 'collector'), 'port')):
                            pass
                            l_2_collector_cli = str_join(((undefined(name='collector_cli') if l_2_collector_cli is missing else l_2_collector_cli), ' port ', environment.getattr(environment.getattr(l_2_exporter, 'collector'), 'port'), ))
                            _loop_vars['collector_cli'] = l_2_collector_cli
                        yield '         '
                        yield str((undefined(name='collector_cli') if l_2_collector_cli is missing else l_2_collector_cli))
                        yield '\n'
                    if t_1(environment.getattr(environment.getattr(l_2_exporter, 'format'), 'ipfix_version')):
                        pass
                        yield '         format ipfix version '
                        yield str(environment.getattr(environment.getattr(l_2_exporter, 'format'), 'ipfix_version'))
                        yield '\n'
                    if t_1(environment.getattr(l_2_exporter, 'local_interface')):
                        pass
                        yield '         local interface '
                        yield str(environment.getattr(l_2_exporter, 'local_interface'))
                        yield '\n'
                    if t_1(environment.getattr(l_2_exporter, 'template_interval')):
                        pass
                        yield '         template interval '
                        yield str(environment.getattr(l_2_exporter, 'template_interval'))
                        yield '\n'
                l_2_exporter = l_2_collector_cli = missing
            if t_1(environment.getattr(l_1_tracker, 'table_size')):
                pass
                yield '      flow table size '
                yield str(environment.getattr(l_1_tracker, 'table_size'))
                yield ' entries\n'
        l_1_tracker = missing
        if t_1(environment.getattr(environment.getattr((undefined(name='flow_tracking') if l_0_flow_tracking is missing else l_0_flow_tracking), 'hardware'), 'shutdown'), False):
            pass
            yield '   no shutdown\n'

blocks = {}
debug_info = '8=18&11=21&12=24&14=26&15=30&16=32&17=35&19=37&20=40&22=42&25=45&26=47&27=52&28=54&29=56&30=58&31=60&33=63&35=65&36=68&38=70&39=73&41=75&42=78&46=81&47=84&50=87&55=90&58=93&59=97&60=99&61=102&63=104&64=107&66=109&69=112&70=114&71=119&72=121&73=123&74=125&75=127&77=130&79=132&80=135&82=137&83=140&85=142&86=145&90=148&91=151&94=154'